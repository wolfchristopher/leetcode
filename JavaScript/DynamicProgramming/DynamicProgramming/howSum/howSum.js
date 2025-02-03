const bruteHowSum = (targetSum, numbers) => {
    if (targetSum === 0) return []
    if (targetSum < 0) return null

    for( let num of numbers) {
        const remainder = targetSum - num
        const remainderResult  =  bruteHowSum(remainder, numbers);
        if (remainderResult !== null) {
            return [ ...remainderResult, num]
        }
    }
    return null
}