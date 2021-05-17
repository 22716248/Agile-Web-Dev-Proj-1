
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
        return 1;
    } else if (password.length <= 12) { // 8 - 12 are ok ( no bonus )
        passStrength += 0; // can restructre later this is redundant
    } else { // passwords over 12 are good!
        passStrength++;
    }

    return passStrength;
}

let displayed = [];
let currentSection = "none";
let sectionIds = ['intro', 'crux', 'aquarius', 'orion-canis-major-taurus', 'centaurus-lupus', 'sagittarius-scorpius', 'argo-navis'];
function fadeIn(sectionId) {
    if (!displayed.includes(sectionId)){
        var fade = document.getElementById('section-' + sectionId);
        var opacity = 0;
        var intervalID = setInterval(function() {
            if (opacity < 1) {
                opacity = opacity + 0.1;
                fade.style.opacity = opacity;
            } else {
                clearInterval(intervalID);
            }
        }, 100);
        displayed.push(sectionId);
    }
}
function updateNav(sectionId) {
    if (!(sectionId == currentSection)) {
        currentSection = sectionId;
        var x;
        var done = false;
        for (x in sectionIds) {
            if (done) {
                document.getElementById(sectionIds[x] + "-nav").className = "nav-icon";
            } else {
                document.getElementById(sectionIds[x] + "-nav").className = "nav-icon-shaded";
            }
            if (currentSection == sectionIds[x]) {
                done = true;
            }
        }
    }

}

$(window).scroll(function() {
    var hT = $('#intro').offset().top,
        hH = $('#intro').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
        console.log((hT-wH) , wS);
    if (wS > (hT+hH-wH)){
        fadeIn('intro');
        updateNav('intro');
    }
});
$(window).scroll(function() {
    var hT = $('#cru').offset().top,
        hH = $('#cru').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
     console.log((hT-wH) , wS);
    if (wS > (hT+hH-wH)){
      fadeIn('crux');
      updateNav('crux');
    }
});
$(window).scroll(function() {
    var hT = $('#aqr').offset().top,
        hH = $('#aqr').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
     console.log((hT-wH) , wS);
    if (wS > (hT+hH-wH)){
        fadeIn('aquarius');
        updateNav('aquarius');
    }
});
$(window).scroll(function() {
    var hT = $('#ori-cma-tau').offset().top,
        hH = $('#ori-cma-tau').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
     console.log((hT-wH) , wS);
    if (wS > (hT+hH-wH)){
        fadeIn('orion-canis-major-taurus');
        updateNav('orion-canis-major-taurus');
    }
});
$(window).scroll(function() {
    var hT = $('#cen-lup').offset().top,
        hH = $('#cen-lup').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
     console.log((hT-wH) , wS);
    if (wS > (hT+hH-wH)){
        fadeIn('centaurus-lupus');
        updateNav('centaurus-lupus');
    }
});
$(window).scroll(function() {
    var hT = $('#sgr-sco').offset().top,
        hH = $('#sgr-sco').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
     console.log((hT-wH) , wS);
    if (wS > (hT+hH-wH)){
        fadeIn('sagittarius-scorpius');
        updateNav('sagittarius-scorpius');
    }
});
$(window).scroll(function() {
    var hT = $('#argo').offset().top,
        hH = $('#argo').outerHeight(),
        wH = $(window).height(),
        wS = $(this).scrollTop();
     console.log((hT-wH) , wS);
    if (wS > (hT+hH-wH)){
        fadeIn('argo-navis');
        updateNav('argo-navis');
    }
});
