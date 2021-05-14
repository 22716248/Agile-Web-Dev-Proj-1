
// Returns the strength of a password given a string
// 1- weak, 2- medium. 3- strong
// can change those around if needed
function passwordStrength(password) {

    let passed_tests;
    //short passwords are automatically weak
    if (password.length < 8){
        return "weak"
    }

    // is has number passed_tests +=1 
    // if has symbol    ""
    // if longer than 20 char ""
    // ect

    // if passed tests > 2 -> medium
    // if "" > 3 -> strong ect
}