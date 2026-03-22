
def kgs_to_lbs(kg):
    cw=float(kg)/0.45
    print(f"Your weight is {cw} pounds")

def lbs_to_kgs(lbs):
    cw=float(lbs)*0.45
    print(f"You are {cw} kilos")

def find_max(nums):
    max = nums[0]
    for num in nums:
        if num > max:
         max = num
    return max