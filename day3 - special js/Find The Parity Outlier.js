const findOutlier = nums => nums.filter(num => num % 2 === 0).length > 1 ? nums.filter(num => num % 2 != 0)[0] : nums.filter(num => num %2 === 0)[0];
