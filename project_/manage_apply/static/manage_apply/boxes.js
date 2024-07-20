document.addEventListener("DOMContentLoaded", function () {
    let elInputUsername = document.querySelector('#number');
    let elFailureMessage = document.querySelector('.failure-message');
    let elInputEmail = document.querySelector('#email');
    let elFailureMessage2 = document.querySelector('.failure-message2');

    // 휴대폰 번호 유효성 검사 정규 표현식
    function checkNumber(value) {
        return /^\d{3}-\d{3,4}-\d{4}$/.test(value);
    }

    // 이메일 유효성 검사 정규 표현식
    function checkEmail(value) {
        return /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i.test(value);
    }

    elInputUsername.onkeyup = function () {
        // 값을 입력한 경우
        if (elInputUsername.value.length !== 0) {
            // 번호 형식이 맞지 않는 경우
            if (checkNumber(elInputUsername.value) === false) {
                elFailureMessage.classList.remove('hide'); // 실패 메시지가 보여야 함
            } else {
                elFailureMessage.classList.add('hide'); // 실패 메시지가 가려져야 함
            }
        } else {
            elFailureMessage.classList.add('hide');
        }
    };

    elInputEmail.onkeyup = function () {
        // 값을 입력한 경우
        if (elInputEmail.value.length !== 0) {
            // 이메일 형식이 맞지 않는 경우
            if (checkEmail(elInputEmail.value) === false) {
                elFailureMessage2.classList.remove('hide'); // 실패 메시지가 보여야 함
            } else {
                elFailureMessage2.classList.add('hide'); // 실패 메시지가 가려져야 함
            }
        } else {
            elFailureMessage2.classList.add('hide');
        }
    };
});

function check_input() {
    const reg_phone = /^\d{3}-\d{3,4}-\d{4}$/;
    const reg_Email = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/i;

    let isValid = true;

    if (!reg_phone.test(document.myForm.number.value)) {
        document.myForm.number.focus();
        alert("휴대폰 번호 형식을 확인해 주세요")
        isValid = false;
    }

    if (!reg_Email.test(document.myForm.email.value)) {
        document.myForm.email.focus();
        alert("이메일 형식을 확인해 주세요")
        isValid = false;
    }

    // 유효하지 않으면 false 반환하여 제출을 방지
    return isValid;
}
