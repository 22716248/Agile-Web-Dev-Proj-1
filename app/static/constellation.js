
// Checks password strength, 0 to 5, very weak to very strong
function passwordStrengthChecker(password) {
    let hasDigit = /\d/;
    let hasBig = /[A-Z]/;
    let hasLittle = /[a-z]/;
    let hasSymbol = /[ `!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
    let passStrength = 0;

    // has numbers
    if (hasDigit.test(password)) {
        passStrength++;
    }
    // has lower case letters
    if (hasBig.test(password)) {
        passStrength++;
    }
    // has upper case letters
    if (hasLittle.test(password)) {
        passStrength++;
    }
    // has symbols
    if (hasSymbol.test(password)) {
        passStrength++;
    }

    // Passwords less than 8 are automatically very weak
    if (password.length < 8) {
        return 0;
    } else if (password.length <= 12) { // 8 - 12 are ok ( no bonus )
        passStrength += 0; // can restructre later this is redundant
    } else { // passwords over 12 are good!
        passStrength++;
    }

    return passStrength;
}