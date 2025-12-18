class Solution {
    largestElement(nums) {
        let L=nums[0]
        for (let i=1; i<nums.length-1;i++){
            if (nums[i]<nums[i+1]){
                L=nums[i+1]
            }
        }
        return L
    }
}
let n=[3, 3, 6, 1]
console.log(new Solution().largestElement(n))
