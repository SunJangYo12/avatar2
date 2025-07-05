import subprocess
import os
import avatar2
import logging


import angr as a #this needs to be carried somewhere

binary = "/media/jin/4abb279b-6d65-4663-97c2-26987f64673a/home/yuna/Tools/avatar/avatar2/examples/binaries/fauxware"
bp_func = "print_test"
bp_func = 0x4007D5 


ava = avatar2.Avatar(arch=avatar2.archs.X86_64,output_directory="/tmp/avatar_angr")
ava.load_plugin("gdb_memory_map_loader")
ava.load_plugin("x86.segment_registers")
# Set log level
#ava.log.setLevel(logging.DEBUG)
ava.log.setLevel(logging.INFO)
print("[+] Creating the GDBTarget")

angr = ava.add_target(avatar2.AngrTarget, binary=binary,load_options={'main_opts': {'backend':'elf'}})


gdb = ava.add_target(avatar2.GDBTarget, local_binary=binary)

print("[+] Initializing the targets")
ava.init_targets()


# untuk relokasi buat angr
cmd = "set environ LD_BIND_NOW=1"
gdb.protocols.execution.console_command(cmd)

gdb.disable_aslr()

print("[+] Running binary until breakpoint")
gdb.bp(bp_func)

# Equivalent to run, but only if not already running
gdb.cont()
gdb.wait()

#state = ava.transfer_state(gdb, angr)


# membaca mapping memori dari gdb, lalu forward ke target lain (angr)
# tujuanya supaya angr memiliki memori map yang sama dengan gdb
# tanpa ini angr akan salah dalam symbolic execution (misalnya mengakses alamat belum dikenal)
ava.load_memory_mappings(gdb, forward=True)



# ini membuat simstate awal untuk angr, yaitu ambil register dari gdb ke state
# simbolik angr, opsi STRICT_PAGE... untuk melarang angr mengakses alamat memori
# diluar page yang diketahui, mirip segfault nyata

# intinya angr seperti otak yang berfikir simbolik, tapi angr ingin mulai dari
# dunia nyata (proses nyata gdb), maka beri angr layout memori asli + nilai register.
options = a.options.common_options | set([a.options.STRICT_PAGE_ACCESS])
s = angr.angr.factory.avatar_state(angr, load_register_from=gdb, options=options)
#s = angr.angr.factory.avatar_state(angr, load_register_from=gdb)



# membuat simulation manager dari state 's'
# simulation dimulai dari kondisi nyata proses di GDB
sm = angr.angr.factory.simgr(s)

# hook semua simbol/fungsi yang ada di proses gdb dengan prosedur simbolik.
angr.hook_symbols(gdb)
sm.explore()

while len(sm.active) > 0:
    print(sm.active[0].regs.pc)
    print(len(sm.active))
    sm.step()

import IPython; IPython.embed()


ava.log.error("End of script")

# Insert angr memory tranfer code here...

