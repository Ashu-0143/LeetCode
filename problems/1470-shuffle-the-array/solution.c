int* shuffle(int* nums, int numsSize, int n, int* returnSize){
int *l=malloc(numsSize*sizeof(int));
for (int j=0,i=0;i<n;i++)
{
    l[i++]=nums[j++];
    l[i]=nums[n++];
}
*returnSize = numsSize;
return l;}
