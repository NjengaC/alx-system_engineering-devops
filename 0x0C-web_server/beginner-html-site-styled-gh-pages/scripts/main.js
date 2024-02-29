const myImage = document.querySelector("img");

myImage.onclick = () => {
	const mySrc = myImage.getAttribute("src");
	if (mySrc === "images/firefox-icon.png") {
		myImage.setAttribute("src", "images/firefox2.png");
	} else {

		myImage.setAttribute("src", "images/firefox-icon.png");
	}
	const buttonA = document.querySelector("#button_A");
	const headingA = document.querySelector("#heading_A");

	buttonA.onclick = () => {
		const name = prompt("What is your name?");
		alert(`Hello ${name}, nice to see you!`);
		headingA.textContent = `Welcome ${name}`;
	};
	let myButton = document.querySelector("button");
	let myHeading = document.querySelector("h1");
	function setUserName() {
		const myName = prompt("Please enter your name.");
		if (!myName) {
			setUserName();
		} else {
			localStorage.setItem("name", myName);
			myHeading.textContent = `Mozilla is cool, ${myName}`;
		}
	}
	if (!localStorage.getItem("name")) {
		setUserName();
	} else {
		const storedName = localStorage.getItem("name");
		myHeading.textContent = `Mozilla is cool, ${storedName}`;
	}

	myButton.onclick = () => {
		setUserName();
	};
	const person = {};

};
