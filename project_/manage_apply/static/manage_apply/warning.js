function addRow() {
    var table = document.getElementById("dynamicTable").getElementsByTagName('tbody')[0];
    var row = table.insertRow();
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
                               
    
    cell1.innerHTML = '<select class="dynamic-select"><option value="A">폐 지르코니아 블록</option><option value="B">폐 지르코니아 분말</option><option value="C">폐 환봉</option><option value="D">폐 밀링툴</option></select>';
    cell2.innerHTML = '<input type="number" step="0.1" min="0">';
    cell3.innerHTML = '<select><option value="1">1</option><option value="2">2</option><option value="3">3</option><option value="4">4">4</option><option value="5">5</option><option value="6">6</option><option value="7">7</option><option value="8">8</option><option value="9">9</option><option value="10">10</option></select>';
    cell4.innerHTML = '<button class="add-row-button" onclick="addRow()">추가</button>';
    cell5.innerHTML = '<button class="delete-row-button" onclick="deleteRow(this)">삭제</button>';
}

function deleteRow(btn) {
    var table = document.getElementById("dynamicTable");
    var rowCount = table.rows.length;
    if (rowCount > 2) { // 최소 1개의 행은 남겨둠
        var row = btn.parentNode.parentNode;
        row.parentNode.removeChild(row);
    } else {
        alert("0개는 선택할 수 없습니다.");
    }
}