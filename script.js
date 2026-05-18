async function addStudent() {

    const name =
        document.getElementById('name').value;

    const roll =
        document.getElementById('roll').value;

    const studentClass =
        document.getElementById('class').value;

    const response = await fetch(
        'https://attendance-system-pied-sigma.vercel.app/',
        {
            method: 'POST',

            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({

                name: name,

                roll_no: roll,

                class: studentClass
            })
        }
    );

    const data = await response.json();

    alert(data.message);

    loadStudents();
}


async function markAttendance() {

    const name =
        document.getElementById('name').value;

    const roll =
        document.getElementById('roll').value;

    const studentClass =
        document.getElementById('class').value;

    const status =
        document.getElementById('status').value;

    const response = await fetch(
        'http://127.0.0.1:5000/mark_attendance',
        {
            method: 'POST',

            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({

                student_name: name,

                roll_no: roll,

                class: studentClass,

                status: status
            })
        }
    );

    const data = await response.json();

    alert(data.message);

    loadAttendance();
}


async function loadStudents() {

    const response = await fetch(
        'https://attendance-system-pied-sigma.vercel.app/'
    );

    const students = await response.json();

    const table =
        document.getElementById('studentTable');

    table.innerHTML = "";

    students.forEach(student => {

        table.innerHTML += `

            <tr>

                <td>${student.name}</td>

                <td>${student.roll_no}</td>

                <td>${student.class}</td>

            </tr>
        `;
    });
}


async function loadAttendance() {

    const response = await fetch(
        'http://127.0.0.1:5000/get_attendance'
    );

    const records = await response.json();

    const table =
        document.getElementById('attendanceTable');

    table.innerHTML = "";

    records.forEach(record => {

        let statusStyle = "";

        if (record.status === "Present") {

            statusStyle =
                "color: green; font-weight: bold;";

        } else {

            statusStyle =
                "color: red; font-weight: bold;";
        }

        table.innerHTML += `

            <tr>

                <td>${record.student_name}</td>

                <td>${record.roll_no}</td>

                <td>${record.class}</td>

                <td style="${statusStyle}">
                    ${record.status}
                </td>

            </tr>
        `;
    });
}


loadStudents();

loadAttendance();
