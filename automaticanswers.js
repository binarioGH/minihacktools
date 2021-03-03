


//done-start - done-complete - done-retry



let video = document.getElementById("home_video_js");

let next = document.getElementsByClassName("FrameRight")[0];


video.addEventListener("ended", function(){next.click()});


let completed = document.getElementsByClassName("done-complete");
let first = document.getElementsByClassName("done-start");
let retry = document.getElementsByClassName("done-retry");
let total = 0;

setInterval(function(){ 
	completed = document.getElementsByClassName("done-complete");
	first = document.getElementsByClassName("done-start");
	retry = document.getElementsByClassName("done-retry");
	let a1 = Array.prototype.slice.call(first, 0);
	let a2 = Array.prototype.slice.call(retry, 0);
	let total_questions = a1.concat(a2);
	for(question of total_questions){
		question.click();
	}
	next.click();
}, 500);