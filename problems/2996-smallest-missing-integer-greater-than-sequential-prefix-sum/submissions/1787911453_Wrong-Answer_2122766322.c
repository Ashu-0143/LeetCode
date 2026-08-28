int missingInteger(int* nums, int numsSize) {
    if (numsSize==1)
        return nums[numsSize-1]+1;
    int sum = nums[0], last = nums[numsSize - 1], max = 0, arr[2500];
    for (int w = 0; w < numsSize; w++) {
            max += nums[w];
        arr[nums[w]] = nums[w];
    }
    for (int i = 1; i < numsSize; i++) {
        if (nums[i] == (nums[i - 1] + 1))
            sum += nums[i];
        else {
            if (arr[sum] == 0)
                return sum;
            else {
                while (sum != max) {
//                    printf("max - %d, sum - %d",max,sum);
                    if (arr[sum] == 0)
                        return sum;
                    sum++;
                }
            }
        }
    }
    return sum;
}
