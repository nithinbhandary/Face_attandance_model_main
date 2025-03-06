
// JavaScript to show remove button when input fields are filled
document.addEventListener('DOMContentLoaded', function() {
    var nameValue = "{{ name }}";
    if (nameValue.trim() !== '') {
        var removeButton = document.querySelector('.remove-button');
        removeButton.style.display = 'block';
    }
});


// function delete_student() {
    // const name = document.getElementById('name').value;
    // const roll_no = document.getElementById('rollno').value;
    // var confirmDelete = confirm("Are you sure you want to remove " + roll_no + "?");
    // if(confirmDelete){
    // fetch('/delete_student', {
        // method: 'POST',
        // headers: {
            // 'Content-Type': 'application/json'
        // },
        // body: JSON.stringify({ name: name, roll_no:roll_no })
    // })
    // .then(response => response.json())
    // .then(data => {
        // console.log('Success:', data);
        // document.getElementById('result').innerText = `Received name: ${data.name} and age: ${data.roll_no}`;
    // })
    // .catch((error) => {
        // console.error('Error:', error);
    // });
// }
// }

function delete_student(){
    window.location.href = "/add_student";
}