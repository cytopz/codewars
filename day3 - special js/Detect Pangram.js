const isPangram = string => Array.from(new Set(string.toLowerCase().split(''))).filter(s => s.match(/[A-Za-z]/g)).sort().join('').trim() === 'abcdefghijklmnopqrstuvwxyz';
