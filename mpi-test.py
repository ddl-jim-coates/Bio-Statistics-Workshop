#!/usr/bin/env python3
import sys
import mpi4py
mpi4py.rc.recv_mprobe = False
from mpi4py import MPI
from socket import gethostname
from random import random as r
from math import pow as p
from time import time

try:
    # Baseline for PI
    PI25DT = 3.141592653589793238462643
    
    # Initialize MPI stuff
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    print(f"Rank {rank}: Starting execution", flush=True)
    
    # Make sure number of attempts (per rank) is given on command line
    if len(sys.argv) != 2:
        if rank == 0:
            print("Error: Please provide number of attempts")
            print("Usage: mpirun -np <processes> python script.py <attempts>")
            print("Example: mpirun -np 4 python script.py 1000000")
        comm.Abort(1)
    
    attempts = int(sys.argv[1])
    local_attempts = int(attempts/size)
    
    if rank == 0:
        print(f"\nComputing {local_attempts} samples on each of the {size} ranks\n", flush=True)
    
    comm.Barrier()
    
    inside = 0.
    tries = 0
    final = 0.
    start_time = time()
    
    # Each rank tries the same number of times
    while tries < local_attempts:
        tries += 1
        if (p(r(),2) + p(r(),2) < 1):
            inside += 1
    
    # Each rank computes a final ratio (float)
    ratio = 4. * (inside/float(local_attempts))
    print(f"[{gethostname()}-{rank:02d}] Local Estimate: {ratio:.16f}   Error: {abs(ratio-PI25DT):.16f}", flush=True)
    
    final_pi = comm.reduce(ratio, op=MPI.SUM, root=0)
    total_time = time() - start_time
    
    # Print the final average from rank 0
    if rank == 0:
        final_pi = final_pi/float(size)
        print(f"\nFinished computing {size*local_attempts} samples in {total_time:.3f} seconds")
        print(f"\nFinal Estimate: {final_pi:.16f}   Error: {abs(final_pi-PI25DT):.16f}")

except ValueError as e:
    print(f"Rank {rank}: Invalid number format: {e}", flush=True)
    if 'comm' in locals():
        comm.Abort(1)
    else:
        sys.exit(1)

except Exception as e:
    print(f"Rank {rank}: Error occurred: {e}", flush=True)
    import traceback
    traceback.print_exc()
    if 'comm' in locals():
        comm.Abort(1)
    else:
        sys.exit(1)