const kebabize = str => str.charAt(0).replace(/[\d-]/g, '').toLowerCase() + str.slice(1).replace(/([A-Z])/g, ' ').split(' ').map(s => s.toLowerCase().replace(/\d/g, '')).join('-');
