#...TTOWG!


def np(nx, ny, nz, N, Pb, bob, co, ce, boi, pi_list, pnow_list):    # 1 mark
    # initializing output variables
    total_np = 0
    np_list = []    # 1 mark
    # the 'for' loops
    for k in range(1,nz+1):
        # fetching pi for the layer from the pi_list
        pi = pi_list[k-1]   # 0.5 mark
        for j in range(1,ny+1):
            for i in range(1,nx+1):
                block_n_order = (nx*ny*(k-1)) + (nx*(j-1)) + i
                # fething pnow for the block from the pnow_list
                Pnow = pnow_list[block_n_order-1]   # 0.5 mark
                bo = bob*(1 - (co*(Pnow - Pb)))
                block_np = (N*boi*ce*(Pi - Pnow))/bo
                total_np = total_np + block_np
                np_list.append(block_np)    # 1 mark
    return total_np, np_list    # 1 mark
            
