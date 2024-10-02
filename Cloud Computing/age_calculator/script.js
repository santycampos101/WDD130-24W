document.getElementById('calculate').addEventListener('click', function() {
    const birthdayInput = document.getElementById('birthday').value;
    if (!birthdayInput) {
        document.getElementById('result').textContent = 'Please enter a valid date.';
        return;
    }
    
    const birthday = new Date(birthdayInput);
    const today = new Date();
    
    let age = today.getFullYear() - birthday.getFullYear();
    const monthDifference = today.getMonth() - birthday.getMonth();
    
    // Adjust age if the birthday hasn't occurred yet this year
    if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthday.getDate())) {
        age--;
    }
    
    document.getElementById('result').textContent = `You are ${age} years old.`;
});
