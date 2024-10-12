function formatTime(date) {
    return (
        date.toLocaleDateString("en-CA") + "+" + date.toLocaleTimeString("en-GB")
    );
}

function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1));
        var temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

const formURL =
    "https://docs.google.com/forms/d/e/1FAIpQLSepkLpC9MCK6ZJdYo5zBz9GIjPrQP5J5VxxXCcaODmDhQDVnw/viewform";

const students = [
    // { studentId: 65070030, name: "จารุกิตติ์ ศรีพาเพลิน" },
    // { studentId: 66070216, name: "อธิบดี  คุ่ยประเสริฐ" },
    // { studentId: 66070139, name: "เพชรแพรทอง  อินอุทัย" }
];

const bookings = [];
let res_begin = new Date("2024-11-01T16:00")
shuffleArray(students)
for (let i = 0; i < 7; i++) {
    students.forEach((student, index) => {
        res_begin.setHours(res_begin.getHours() + 3)
        const res_end = new Date(res_begin);
        res_end.setHours(res_end.getHours() + 3);

        const entryData = [
            { id: 1822805640, value: student.studentId }, // Student ID
            { id: 1353161969, value: student.name }, // Reserver Name
            { id: 2141265806, value: "-" }, // Phone Number
            // { id: 93529149, value: "ห้อง Peer tutor 2" }, // Room
            { id: 93529149, value: "ห้อง Creative and Ideation 1" }, // Room
            { id: 492172744, value: formatTime(res_begin) }, // Begin Time
            { id: 445633396, value: formatTime(res_end) }, // End Time
            { id: 1851518935, value: "__other_option__", other: "เตรียมแข่ง Huawei ICT" }, // Purpose
        ];

        const url = new URL(formURL);
        entryData.forEach((entry) => {
            url.searchParams.append(`entry.${entry.id}`, entry.value);
            if (entry.other) {
                url.searchParams.append(
                    `entry.${entry.id}.other_option_response`,
                    entry.other
                );
            }
        });

        bookings.push(url.toString());
    });
    res_begin.setDate(res_begin.getDate() + 1);
    res_begin.setHours(16);
}

console.log(bookings); // Output an array of URLs for each booking