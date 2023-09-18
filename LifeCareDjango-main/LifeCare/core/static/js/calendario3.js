const currentDate = document.querySelector(".current-date");
daysTag           = document.querySelector(".days");
prevNextIcon      = document.querySelectorAll(".icons span");

// Getting New Date, Current Year and Month

let date  = new Date(),
currYear  = date.getFullYear(),
currMonth = date.getMonth();

//console.log(date, currYear, currMonth)
//console.log(currYear)
//console.log(currMonth)
//console.log(currentDate)


const months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
				"Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

const renderCalendar = () => {
	// Getting First Day/Last Date/Day of Month and Last Date of Last Month
	let firstDayofMonth     = new Date(currYear, currMonth, 1).getDay();
	let lastDateofMonth     = new Date(currYear, currMonth + 1, 0).getDate();
	let lastDayofMonth      = new Date(currYear, currMonth, lastDateofMonth).getDay();
	let lastDateofLastMonth = new Date(currYear, currMonth, 0).getDate();
	let liTag = "";

	// Creating li of previous month last days
	for (let i = firstDayofMonth; i > 0; i--) {
		liTag += `<li class="inactive">${lastDateofLastMonth - i + 1}</li>`;
	}

	// Creating li of all days of current month
	for (let i = 1; i <= lastDateofMonth; i++) {
		// Adding active class to li if the current day, month, and year matched
		let isToday = i === date.getDate() && currMonth === new Date().getMonth()
						&& currYear === new Date().getFullYear() ? "active" : "";
		liTag += `<li class="${isToday}">${i}</li>`;
	}

	// Creating li of next month first days
	for (let i = lastDayofMonth; i < 6; i++) {
		liTag += `<li class="inactive">${i - lastDayofMonth + 1}</li>`;
	}

	// Return Current Month and Year
	currentDate.innerText = `${months[currMonth]} ${currYear}`;

	// Insert liTag in HTML
	daysTag.innerHTML = liTag;
}
renderCalendar();

prevNextIcon.forEach(icon => {
	// Agregando el Evento Click en ambos íconos < >
	icon.addEventListener("click", () => {

		// if clicked icon is previous icon then decrement currentMonth by 1 
		// else increment it by 1
		currMonth = icon.id === "prev" ? currMonth - 1 : currMonth + 1;

		// if current month is less than 0 o greater than 11
		if (currMonth < 0 || currMonth > 11) {
			// Creating a new date of current year & month and pass it as date value
			date = new Date(currYear, currMonth);
			currYear  = date.getFullYear(); // Updating current year with new date year
			currMonth = date.getMonth(); // Updating current month with new date month
		} else { // else pass new Date as date value
			date = new Date();
		}
		renderCalendar();
	});
});

