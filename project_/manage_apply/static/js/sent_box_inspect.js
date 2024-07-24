// 기존의 유효성 검사 함수들

// 폰번호 확인
function checkNumber(value) {
    return /^\d{3}-\d{3,4}-\d{4}$/.test(value);
}

// 작성여부 확인
function checkNormal(value) {
    return value.trim() === "";
}

// 문자열 길이 확인 (10자 이하로 제한)
function checkLen(value) {
    return value.length > 10;
}

// 송장번호 확인
function checkInvoiceNumber(value) {
    return /^\d{3}-\d{4}-\d{4}$/.test(value);
}

// 폐기물 종류 검사
function checkWaste() {
    let z_b_kg = parseFloat(document.getElementById('z_b_kg').value);
    let z_b_num = parseInt(document.getElementById('z_b_num').value);
    let z_p_kg = parseFloat(document.getElementById('z_p_kg').value);
    let z_p_num = parseInt(document.getElementById('z_p_num').value);
    let r_b_kg = parseFloat(document.getElementById('r_b_kg').value);
    let r_b_num = parseInt(document.getElementById('r_b_num').value);
    let tool_kg = parseFloat(document.getElementById('tool_kg').value);
    let tool_num = parseInt(document.getElementById('tool_num').value);

    return (z_b_kg >= 0.1 && z_b_num >= 1) ||
           (z_p_kg >= 0.1 && z_p_num >= 1) ||
           (r_b_kg >= 0.1 && r_b_num >= 1) ||
           (tool_kg >= 0.1 && tool_num >= 1);
}

document.addEventListener("DOMContentLoaded", function () {
    let elInput_Comapany = document.querySelector('#company');
    let elInput_Com_num = document.querySelector('#com_num');
    let elInput_applicant = document.querySelector('#applicant');
    let elInput_apcan_phone = document.querySelector('#apcan_phone');
    let elInput_delivery_num = document.querySelector('#delivery_num');
    let elCheckbox = document.querySelector('#flexCheckDefault');

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

    elInput_delivery_num.onkeyup = function () {
        if (elInput_delivery_num.value.length !== 0) {
            if (!checkInvoiceNumber(elInput_delivery_num.value)) {
                document.querySelector('.warning.delivery_num').style.display = 'block';
            } else {
                document.querySelector('.warning.delivery_num').style.display = 'none';
            }
        } else {
            document.querySelector('.warning.delivery_num').style.display = 'block';
        }
    };

    elCheckbox.onchange = function () {
        if (!elCheckbox.checked) {
            document.querySelector('.warning.flexCheckDefault').style.display = 'block';
        } else {
            document.querySelector('.warning.flexCheckDefault').style.display = 'none';
        }
    };
});

function check_input() {
    const reg_phone = /^\d{3}-\d{3,4}-\d{4}$/;

    if (checkNormal(document.box_form['company'].value) || checkLen(document.box_form['company'].value)) {
        document.box_form.company.focus();
        alert("회사명을 정확히 작성해 주세요(10자 이하)");
        return false;
    }

    if (!checkNormal(document.box_form['com_num'].value) && !checkNumber(document.box_form['com_num'].value)) {
        document.box_form.com_num.focus();
        alert("회사 연락처를 형식에 맞게 작성해 주세요");
        return false;
    }

    if (checkNormal(document.box_form['applicant'].value) || checkLen(document.box_form['applicant'].value)) {
        document.box_form.applicant.focus();
        alert("담당자 성함을 정확히 작성해 주세요(10자 이하)");
        return false;
    }

    if (checkNormal(document.box_form['apcan_phone'].value) || !checkNumber(document.box_form['apcan_phone'].value)) {
        document.box_form.apcan_phone.focus();
        alert("담당자 연락처를 정확히 작성해 주세요");
        return false;
    }

    if (!checkInvoiceNumber(document.box_form['delivery_num'].value)) {
        document.box_form.delivery_num.focus();
        document.querySelector('.warning.delivery_num').style.display = 'block';
        alert("송장번호를 정확히 작성해 주세요");
        return false;
    }

    if (!document.getElementById('flexCheckDefault').checked) {
        document.getElementById('flexCheckDefault').focus();
        document.querySelector('.warning.flexCheckDefault').style.display = 'block';
        alert("개인정보 수집 및 이용에 동의해주세요");
        return false;
    }

    if (!checkWaste()) {
        alert("적어도 한 종류의 폐기물 무게가 0.1kg 이상이고 개수가 1개 이상이어야 합니다.");
        return false;
    }

    return true;
}
