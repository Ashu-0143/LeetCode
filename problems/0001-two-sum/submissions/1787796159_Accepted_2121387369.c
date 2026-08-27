
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i = 0, sum, temp2;
    int* a = malloc(2 * sizeof(int));
    a[0] = 0;
    a[1] = 0;

    for (i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            sum = nums[i] + nums[j];
            if (sum == target) {
                a[0] = i;
                a[1] = j;
                *returnSize = 2;
                return a;
            }
        }
        sum = 0;
    }
    return a;
}
