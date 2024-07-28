// 전화번호 형식 확인 (xxx-xxx(x)-xxxx)
function checkNumber(value) {
    return /^\d{3}-\d{3,4}-\d{4}$/.test(value) || /^\d{10,11}$/.test(value);
}

// 값이 비어있는지 확인
function checkNormal(value) {
    return value.trim() === "";
}

// 문자열 길이 확인 (10자 이하로 제한)
function checkLen(value) {
    return value.length > 10;
}

// 송장번호 형식 확인
function checkInvoiceNumber(value) {
    return /^\d{12}$/.test(value);
}

// 문서 로드가 완료되었을 때 실행되는 함수
document.addEventListener("DOMContentLoaded", function () {
    // 각 입력 요소 가져오기
    let elInput_Comapany = document.querySelector('#company');
    let elInput_Com_num = document.querySelector('#com_num');
    let elInput_applicant = document.querySelector('#applicant');
    let elInput_apcan_phone = document.querySelector('#apcan_phone');
    let elInput_delivery_num = document.querySelector('#delivery_num');
    let elCheckbox = document.querySelector('#flexCheckDefault');

    // 회사명 입력 시 유효성 검사
    elInput_Comapany.onkeyup = function () {
        if (elInput_Comapany.value.length !== 0) {
            if (checkNormal(elInput_Comapany.value) || checkLen(elInput_Comapany.value)) {
                document.querySelector('.warning.company').style.display = 'block';
            } else {
                document.querySelector('.warning.company').style.display = 'none';
            }
        } else {
            document.querySelector('.warning.company').style.display = 'block';
        }
    };

    // 회사 연락처 입력 시 유효성 검사
    elInput_Com_num.onkeyup = function () {
        if (elInput_Com_num.value.length !== 0) {
            if (!checkNormal(elInput_Com_num.value) && !checkNumber(elInput_Com_num.value)) {
                document.querySelector('.warning.com_num').style.display = 'block';
            } else {
                document.querySelector('.warning.com_num').style.display = 'none';
            }
        } else {
            document.querySelector('.warning.com_num').style.display = 'block';
        }
    };

    // 담당자 성함 입력 시 유효성 검사
    elInput_applicant.onkeyup = function () {
        if (elInput_applicant.value.length !== 0) {
            if (checkNormal(elInput_applicant.value) || checkLen(elInput_applicant.value)) {
                document.querySelector('.warning.applicant').style.display = 'block';
            } else {
                document.querySelector('.warning.applicant').style.display = 'none';
            }
        } else {
            document.querySelector('.warning.applicant').style.display = 'block';
        }
    };

    // 담당자 연락처 입력 시 유효성 검사
    elInput_apcan_phone.onkeyup = function () {
        if (elInput_apcan_phone.value.length !== 0) {
            if (checkNormal(elInput_apcan_phone.value) || !checkNumber(elInput_apcan_phone.value)) {
                document.querySelector('.warning.apcan_phone').style.display = 'block';
            } else {
                document.querySelector('.warning.apcan_phone').style.display = 'none';
            }
        } else {
            document.querySelector('.warning.apcan_phone').style.display = 'block';
        }
    };

    // 송장번호 입력 시 유효성 검사
    elInput_delivery_num.onkeyup = function () {
        if (elInput_delivery_num.value.length !== 0) {
            if (!checkInvoiceNumber(elInput_delivery_num.value)|| !checkInvoiceNumber(elInput_delivery_num.value)) {
                document.querySelector('.warning.delivery_num').style.display = 'block';
            } else {
                document.querySelector('.warning.delivery_num').style.display = 'none';
            }
        } else {
            document.querySelector('.warning.delivery_num').style.display = 'block';
        }
    };

    // 개인정보 수집 및 이용 동의 체크박스 변경 시 유효성 검사
    elCheckbox.onchange = function () {
        if (!elCheckbox.checked) {
            document.querySelector('.warning.flexCheckDefault').style.display = 'block';
        } else {
            document.querySelector('.warning.flexCheckDefault').style.display = 'none';
        }
    };
});

// 폼 제출 시 입력 값 유효성 검사 함수
function check_input() {
    const reg_phone = /^\d{3}-\d{3,4}-\d{4}$/;

    // 폐기물 종류 유효성 검사
    if (!checkWaste()) {
        alert("적어도 한 종류의 폐기물의 개수가 1개 이상이어야 합니다.");
        return false;
    }

    // 회사명 유효성 검사
    if (checkNormal(document.box_form['company'].value) || checkLen(document.box_form['company'].value)) {
        document.box_form.company.focus();
        alert("회사명을 정확히 작성해 주세요(10자 이하)");
        return false;
    }

    // 회사 연락처 유효성 검사
    if (!checkNormal(document.box_form['com_num'].value) && !checkNumber(document.box_form['com_num'].value)) {
        document.box_form.com_num.focus();
        alert("회사 연락처를 형식에 맞게 작성해 주세요");
        return false;
    }

    // 담당자 성함 유효성 검사
    if (checkNormal(document.box_form['applicant'].value) || checkLen(document.box_form['applicant'].value)) {
        document.box_form.applicant.focus();
        alert("담당자 성함을 정확히 작성해 주세요(10자 이하)");
        return false;
    }

    // 담당자 연락처 유효성 검사
    if (checkNormal(document.box_form['apcan_phone'].value) || !checkNumber(document.box_form['apcan_phone'].value)) {
        document.box_form.apcan_phone.focus();
        alert("담당자 연락처를 정확히 작성해 주세요");
        return false;
    }

    // 송장번호 유효성 검사
    if (!checkInvoiceNumber(document.box_form['delivery_num'].value)) {
        document.box_form.delivery_num.focus();
        document.querySelector('.warning.delivery_num').style.display = 'block';
        alert("송장번호를 정확히 작성해 주세요");
        return false;
    }

    // 개인정보 수집 및 이용 동의 체크 여부 검사
    if (!document.getElementById('flexCheckDefault').checked) {
        document.getElementById('flexCheckDefault').focus();
        document.querySelector('.warning.flexCheckDefault').style.display = 'block';
        alert("개인정보 수집 및 이용에 동의해주세요");
        return false;
    }

    // 폼 제출
    document.box_form.submit();
    return true;
}
