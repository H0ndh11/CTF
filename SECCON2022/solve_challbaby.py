import angr
import claripy

p=angr.Project('./chall.baby', auto_load_libs=False)

argv1 = claripy.BVS("argv1",100*8)
#addr_main=p.loader.main_object.get_symbol('main').linked_addr+0x400000
addr_succeeded=0x12cc+0x400000
addr_failed=[0x1273+0x400000, 0x12d3+0x400000]

#コマンドライン引数argv1があることを指定
initial_state = p.factory.entry_state(args=["./chall.baby",argv1])

simmgr=p.factory.simulation_manager(initial_state)

simmgr.explore(find=addr_succeeded,avoid=addr_failed)
found=simmgr.found[0]
solution=found.solver.eval(argv1, cast_to=bytes)

print(repr(solution))
solution = solution[:solution.find(b"\x00")]
print(solution)