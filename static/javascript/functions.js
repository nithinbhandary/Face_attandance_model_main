function showLoadingScreen() {
        document.getElementById('loading-screen').style.display = 'flex';
    }
function viewAttendance() {
        window.location.href = "/attendance_view";
}
function TakeAttendance() {
        showLoadingScreen();
        window.location.href = "/takeattendance";
}
function Addstudent() {
        showLoadingScreen();
        window.location.href = "/add_student";
}
// function viewAttendance() {
//         window.location.href = "/attendance_view";
// }
// function TakeAttendance() {
//         window.location.href = "/takeattendance";
// }
// function Addstudent() {
//         window.location.href = "/add_student";
// }

function Search_stuentd(){
    window.location.href = "/search_rollno";
}

function backhome() {
        window.location.href = "/backhome";
}
    
function delete_student(){
        window.location.href = "/search_rollno";
}
    
// function delete_student(this,rollno,name){
        // window.location.href = "/remove_student"+name+rollno;
// }

//function delete_student(this, rollno, name) {
//             var confirmDelete = confirm("Are you sure you want to remove " + name + "?");
//             if (confirmDelete){
//                     console.log("Removing student with Roll No: " + rollno);
//                     console.log("Student Name: " + name);
//                     // window.location.href = "/remove_student"+name+rollno;
//                     var redirectUrl = `/delete_student?rollno=${encodeURIComponent(rollno)}&name=${encodeURIComponent(name)}`;
//                     // Redirect to the constructed URL
//                     window.location.href = redirectUrl;
//             }
//        }
// // JavaScript to show remove button when input fields are filled
// document.addEventListener('DOMContentLoaded', function() {
//         var nameValue = "{{ name }}";
//         if (nameValue.trim() !== '') {
//             var removeButton = document.querySelector('.remove-button');
//             removeButton.style.display = 'block';
//         }
// });
// function delete_student(this, rollno, name) {
//         var confirmDelete = confirm("Are you sure you want to remove " + name + "?");
//         if (confirmDelete){
//                 console.log("Removing student with Roll No: " + rollno);
//                 console.log("Student Name: " + name);
//                 // window.location.href = "/remove_student"+name+rollno;
//                 var redirectUrl = `/delete_student?rollno=${encodeURIComponent(rollno)}&name=${encodeURIComponent(name)}`;

//                 // Redirect to the constructed URL
//                 window.location.href = redirectUrl;
//         }
//         // var table = document.getElementById("student-table");
//         // var rows = table.getElementsByTagName("tr");
//         // for (var i = 0; i < rows.length; i++) {
//         //     var currentRow = rows[i];
//         //     var currentButton = currentRow.querySelector('.remove-button');
//         //     if (currentButton === button) {
//         //         currentRow.remove();
//         //     } else {
//         //         // Clear other rows
//         //         currentRow.querySelector('td:nth-child(1)').innerText = "";
//         //         currentRow.querySelector('td:nth-child(2)').innerText = "";
//         //     }
//         // }
//     }


function Search_stuentd(){
    window.location.href = "/search_rollno";
}

function backhome(){
        window.location.href="/backhome";
}

// function delete_student(this,rollno,name){
        // window.location.href = "/remove_student"+name+rollno;
// }

//function delete_student(this, rollno, name) {
//             var confirmDelete = confirm("Are you sure you want to remove " + name + "?");
//             if (confirmDelete){
//                     console.log("Removing student with Roll No: " + rollno);
//                     console.log("Student Name: " + name);
//                     // window.location.href = "/remove_student"+name+rollno;
//                     var redirectUrl = `/delete_student?rollno=${encodeURIComponent(rollno)}&name=${encodeURIComponent(name)}`;
//                     // Redirect to the constructed URL
//                     window.location.href = redirectUrl;
//             }
//        }
// // JavaScript to show remove button when input fields are filled
// document.addEventListener('DOMContentLoaded', function() {
//         var nameValue = "{{ name }}";
//         if (nameValue.trim() !== '') {
//             var removeButton = document.querySelector('.remove-button');
//             removeButton.style.display = 'block';
//         }
// });
// function delete_student(this, rollno, name) {
//         var confirmDelete = confirm("Are you sure you want to remove " + name + "?");
//         if (confirmDelete){
//                 console.log("Removing student with Roll No: " + rollno);
//                 console.log("Student Name: " + name);
//                 // window.location.href = "/remove_student"+name+rollno;
//                 var redirectUrl = `/delete_student?rollno=${encodeURIComponent(rollno)}&name=${encodeURIComponent(name)}`;

//                 // Redirect to the constructed URL
//                 window.location.href = redirectUrl;
//         }
//         // var table = document.getElementById("student-table");
//         // var rows = table.getElementsByTagName("tr");
//         // for (var i = 0; i < rows.length; i++) {
//         //     var currentRow = rows[i];
//         //     var currentButton = currentRow.querySelector('.remove-button');
//         //     if (currentButton === button) {
//         //         currentRow.remove();
//         //     } else {
//         //         // Clear other rows
//         //         currentRow.querySelector('td:nth-child(1)').innerText = "";
//         //         currentRow.querySelector('td:nth-child(2)').innerText = "";
//         //     }
//         // }
//     }

