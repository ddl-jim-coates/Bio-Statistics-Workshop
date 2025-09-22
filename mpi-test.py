#!/usr/bin/env python3
import sys
import os

print(f"DEBUG: Script started, PID: {os.getpid()}")
print(f"DEBUG: Python version: {sys.version}")
print(f"DEBUG: Arguments: {sys.argv}")
print(f"DEBUG: Working directory: {os.getcwd()}")

try:
    print("DEBUG: Importing mpi4py...")
    import mpi4py
    mpi4py.rc.recv_mprobe = False
    from mpi4py import MPI
    print("DEBUG: mpi4py imported successfully")
    
    from socket import gethostname
    from random import random as r
    from math import pow as p
    from time import time
    
    # Initialize MPI stuff
    print("DEBUG: Initializing MPI...")
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    
    print(f"DEBUG: MPI initialized - Size: {size}, Rank: {rank}, Host: {gethostname()}")
    
    # Baseline for PI
    PI25DT = 3.141592653589793238462643
    
    # Check command line arguments
    print(f"DEBUG: Checking arguments... len(sys.argv) = {len(sys.argv)}")
    if len(sys.argv) != 2:
        if rank == 0:
            print("ERROR: Please provide number of attempts")
            print("Usage: mpirun -np <processes> python script.py <attempts>")
            print("Example: mpirun -np 4 python script.py 1000000")
        print(f"DEBUG: Rank {rank} exiting due to argument error")
        comm.Abort(1)
    
    attempts = int(sys.argv[1])
    local_attempts = int(attempts/size)
    
    if rank == 0:
        print(f"\nComputing {local_attempts} samples on each of the {size} ranks")
        print(f"Total samples: {size * local_attempts}\n")
    
    print(f"DEBUG: Rank {rank} will process {local_attempts} samples")
    
    comm.Barrier()
    print(f"DEBUG: Rank {rank} passed barrier, starting computation...")
    
    inside = 0.
    tries = 0
    start_time = time()
    
    # Each rank tries the same number of times
    while tries < local_attempts:
        tries += 1
        if (p(r(),2) + p(r(),2) < 1):
            inside += 1
        
        # Progress for rank 0
        if rank == 0 and tries % (local_attempts // 10) == 0:
            print(f"DEBUG: Rank {rank} progress: {tries}/{local_attempts}")
    
    print(f"DEBUG: Rank {rank} completed computation. Inside: {inside}, Tries: {tries}")
    
    # Each rank computes a final ratio (float)
    ratio = 4. * (inside/float(local_attempts))
    computation_time = time() - start_time
    
    print(f"[{gethostname()}-{rank:02d}] Local Estimate: {ratio:.16f}   Error: {abs(ratio-PI25DT):.16f}   Time: {computation_time:.3f}s", flush=True)
    
    print(f"DEBUG: Rank {rank} about to reduce...")
    final_pi = comm.reduce(ratio, op=MPI.SUM, root=0)
    total_time = time() - start_time
    
    print(f"DEBUG: Rank {rank} completed reduce operation")
    
    # Print the final average from rank 0
    if rank == 0:
        final_pi = final_pi/float(size)
        print(f"\n" + "="*50)
        print(f"FINAL RESULTS:")
        print(f"Total samples: {size*local_attempts}")
        print(f"Total time: {total_time:.3f} seconds")
        print(f"Final Pi estimate: {final_pi:.16f}")
        print(f"Actual Pi: {PI25DT:.16f}")
        print(f"Final error: {abs(final_pi-PI25DT):.16f}")
        print("="*50)
    
    print(f"DEBUG: Rank {rank} finished successfully")

except ImportError as e:
    print(f"IMPORT ERROR: {e}")
    print("Make sure mpi4py is installed: pip install mpi4py")
    sys.exit(1)

except ValueError as e:
    print(f"Rank {rank if 'rank' in locals() else '?'}: Invalid number format: {e}")
    if 'comm' in locals():
        comm.Abort(1)
    else:
        sys.exit(1)

except Exception as e:
    print(f"Rank {rank if 'rank' in locals() else '?'}: Error occurred: {e}")
    import traceback
    traceback.print_exc()
    if 'comm' in locals():
        comm.Abort(1)
    else:
        sys.exit(1)