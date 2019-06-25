#planned_blocks = [0,1,2,4,5,6,7,8,9,9,9,8,9]
#planned_blocks = [9,8,7,8,9,2,9,9,5,6]
planned_blocks = [0,0,0,0,6,1,2,0]
built_blocks = planned_blocks.copy()

def fill_blocks(construction_of_blocks):
    def check_blocks(construction_of_blocks):
        max_value = max(construction_of_blocks)
        max_value_index = construction_of_blocks.index(max_value)

        # All the block stacks up the the tallest block stack
        start_to_max = construction_of_blocks[:max_value_index]

        # All the block stacks from the tallest block stack to the end of the stacks
        max_to_end = construction_of_blocks[max_value_index:]

        # Check that the blocks are "filled with water" 
            # I.e. They are ordered so that the:
                #  Values to the left and right of the highest value are smaller than the highest value. 
                    ## from 0 to max = sorted asc 
                    ## from max to end = sorted desc 
        if ((sorted(start_to_max) == start_to_max) and (sorted(max_to_end, reverse=True)) == max_to_end):
            return True
    
    # while the blocks are not "filled" keep adding water ;)
    while check_blocks(construction_of_blocks) != True:
        maxi = construction_of_blocks[0]
        for idx, block in enumerate(construction_of_blocks):
            if idx ==0:
                prev_block = block
            else:
                prev_block = construction_of_blocks[idx-1]

            if (block > prev_block and block <= maxi):
                construction_of_blocks[idx-1] = block
            if (block > maxi):
                maxi = block

        return fill_blocks(construction_of_blocks)
    return construction_of_blocks

built_blocks = fill_blocks(built_blocks)

print('built ',built_blocks)
print('planned ',planned_blocks)
result = [a - b for a, b in zip(built_blocks,planned_blocks)]
print('result ',result)

total_water = 0
for i in result: 
    total_water+=i
print('Total blocks filled with water = ',total_water)    
