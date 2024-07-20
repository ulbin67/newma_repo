// script.js
let currentIndex = 0;
// 현재 슬라이드의 인덱스를 저장하는 변수
// 처음에는 첫번째 슬라이드를 가리킴
//function showSlide(index) {...}: 인덱스에 해당하는 슬라이드를 보여주는 함수입니다. 슬라이드의 인덱스를 받아와서 currentIndex를 업데이트하고, 슬라이드 컨테이너의 transform 스타일을 변경하여 슬라이드를 이동시킵니다.
//function moveSlides(direction) {...}: 슬라이드를 이동시키는 함수입니다. direction은 슬라이드 이동 방향을 나타내며, -1이면 이전 슬라이드로, 1이면 다음 슬라이드로 이동합니다.
//let slideInterval = setInterval(() => { moveSlides(1); }, 3000);: 3초마다 자동으로 슬라이드를 이동시키는 타이머를 설정합니다.
//slider.addEventListener('mouseover', () => clearInterval(slideInterval));: 슬라이더 위에 마우스가 올라가면 자동 슬라이드쇼를 일시 정지합니다.
//slider.addEventListener('mouseout', () => { slideInterval = setInterval(() => { moveSlides(1); }, 3000); });: 슬라이더에서 마우스가 벗어나면 자동 슬라이드쇼를 다시 시작합니다.

function showSlide(index) {
    const slides = document.querySelector('.slides');
    const totalSlides = document.querySelectorAll('.slide').length;

    if (index >= totalSlides) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = totalSlides - 1;
    } else {
        currentIndex = index;
    }

    const offset = -currentIndex * 100;
    slides.style.transform = `translateX(${offset}%)`;
}

function moveSlides(direction) {
    showSlide(currentIndex + direction);
}


