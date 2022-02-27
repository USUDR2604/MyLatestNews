document.querySelector(".Carousel-Content-Sty").classList.add('slider');
var slidings = document.querySelectorAll('.Automobile-content');
var slide = document.querySelectorAll('.main-card');
//Setting Up All
let i = 0;
for (i = 0; i < slidings.length; i++) {
    let slideid = "js-slider-" + i;
    slidings[i].classList.add('slide');
    slidings[i].setAttribute('id', slideid);
    let prev = document.createElement('a');
    prev.classList.add('prev-sty');
    slide[i].appendChild(prev);
    let next = document.createElement('a');
    next.classList.add('next-sty');
    slide[i].appendChild(next);
    //Add Count
    let addnum = 1;
    let len = slidings.length;
    //prev id
    let lnum = parseInt(i) - parseInt(addnum);
    if (lnum === -1) {
        lnum = parseInt(len) - parseInt(addnum);
    }

    previd = "#js-slider-" + lnum;
    prev.setAttribute("href", previd);
    //Succ Id
    let snum = parseInt(i) + parseInt(addnum);
    if (snum === len) {
        snum = 1;
    }
    nextid = "#js-slider-" + snum;
    next.setAttribute("href", nextid);
}