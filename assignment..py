def mat_bal(nx, ny, nz, N, boi, bob, ce, co, Pb, Pi, Pnow_list):
    total_np = 0
    np_list = []
    for k in range(1, nz+1):
        for j in range(1, ny+1):
            for i in range(1, nx+1):
                block_n_order = nx*(j-1) + i
                Pnow = Pnow_list[(block_n_order + 1)]
                bo = bob*(1 - (co*(Pnow - Pb)))
                block_np = (N*boi*ce*(Pi - Pnow))/bo
                np_list.append(block_np)
                total_np = total_np + block_np
    return bo, total_np, np_list
        
    
