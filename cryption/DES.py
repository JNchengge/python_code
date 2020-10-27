def separate_key_blocks(key):
    key_sequence=''
    key_blocks=[]
    for character in key: #密钥转二进制
        key_sequence+='{:0>8}'.format(format(ord(character),'b'))
        key_blocks.append('{:0>8}'.format(format(ord(character),'b')))
    #print(key_sequence)
    #print(len(key_sequence))
    #print(key_blocks)
    key_C=key_blocks[0]+key_blocks[1]+key_blocks[2]+key_blocks[3]  #C组
    key_D=key_blocks[4]+key_blocks[5]+key_blocks[6]+key_blocks[7]  #D组
    key_blocks=[key_C,key_D]  #C组和D组的集合
    return key_blocks
def circular_shift_left(bin_sequence,k):  #根据参数k做左循环位移
    shifted_bin_sequence=bin_sequence[k:]+bin_sequence[:k]
    return shifted_bin_sequence
def del_last_num(key_blocks):     #删除每8bit的最后一位
    for key_block in key_blocks:
        temp=''
        for i in range(0,32):
            if i!=7 and i!=15 and i!=23 and i!=31:
                temp+=key_block[i]
        key_block=temp
    return key_blocks
def ip_iteration(key_blocks):                                               #IP置换
    key_sq_origin=''                                                        #原密钥序列
    key_sq_intered=''                                                       #修改后的密钥序列
    ip=[  58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
		62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
		57, 49, 41, 33, 25, 17,  9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
		61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7 ]
    for key_block in key_blocks:                                            #拼接C、D到原密钥序列
        key_sq_origin+=key_block 
    for i in ip:                                                            #置换
        key_sq_intered+=key_sq_origin[i-1]
    key_blocks_itered=[key_sq_intered[i:i+32] for i in [0,32]]
    return key_blocks_itered
def PC_2_interation(key_sq):               #PC_2置换，每次只操作一个序列
    key_sq_itered=''

    PC_2=[ 14, 17, 11, 24, 1,   5,
		    3, 28, 15,  6, 21, 10,
			23, 19, 12,  4, 26,  8,
			16,  7, 27, 20, 13,  2,
			41, 52, 31, 37, 47, 55,
			30, 40, 51, 45, 33, 48,
			44, 49, 39, 56, 34, 53,
			46, 42, 50, 36, 29, 32 ]

    for j in PC_2:                             
        key_sq_itered+=key_sq[PC_2[j]-1]
    
    return key_sq_itered
def yeild_16rounds_key(key_blocks):                         #生成16轮密钥
    LS = [ 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2,2, 1 ]
    for i in LS:
        key_blocks[0]=circular_shift_left(key_blocks[0],i)  #C组左移
        key_blocks[1]=circular_shift_left(key_blocks[1],i)  #D组左移
        key_sq=key_blocks[0]+key_blocks[1]                  #C、D拼接
        key_sq=key_sq[0:49]                                 #取前48位
        key_sq=PC_2_interation(key_sq)                      #PC_2置换
        yield key_sq                                        #生成器



    



        













