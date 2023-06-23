$(document).ready(function(){ 	//When the document is read or completely loaded. 
	
	var c = $('canvas')[0];	 //Grabs the canvas element.   
	
	var ctx = c.getContext("2d");  //Creates a convex object for two-dim drawing.

	var heapType = ""; //Type of the heap tree. 

	var heap; //The Binary heap data structure. 

	var level_distances = [250,125,62.5,31.25,15.625,7.8125,3.90625,1.953125];

	$('canvas').attr({   //Sets the canvas element with the dimensions of the parent div. 
		'width': $('.myCanvas').outerWidth(),
		'height':$('.myCanvas').outerHeight()
	});

	$('.add-button').click(function(){  //If the add button is clicked gets the height of the parent div and increases it by 50px.
		var isValidValue = false;	//Used to check if user input is valid.

		if($('.contentInput').val() != '') //Checks the user input to add if its not undefined the its a valid value.
			isValidValue = true;


		if(isValidValue){	//If valid proceed
			var item = $('.contentInput').val();
			heap.insert(parseInt(item));
			heap.showBinaryHeap();
			drawTree(c.width/2,25,0,0)
		}
		else{	//Otherwise display a helpful tip.
			$('.infoContent-block .popup').show();
			$('.infoContent-block .popup').delay(3000).fadeOut();
		}

			/*var test = $('.myCanvas').outerHeight();
			test += 50; 
			$('.myCanvas').height(test);
			adjustContent(); */
	});
	
	$('.remove-button').on("click",function(){ 
		heap.remove();	//Removes from the heap.
		heap.showBinaryHeap();
		
		ctx.clearRect(0,0, $('.myCanvas').outerWidth(), $('.myCanvas').outerHeight());

		drawTree(c.width/2,25,0,0);

			/*var test = $('.myCanvas').outerHeight();
			test -= 50; 
			$('.myCanvas').height(test);
			adjustContent();*/ 
	});

	$(".submit-button").on("click",function(){ 		//When the submit button is clicked.
		var isValidType = false;	//Used to check if user input a valid heap type.

		if($('.infoInput').val().toLowerCase() === 'min' || $('.infoInput').val().toLowerCase() === 'max'){ //Checks if user input is valid.
			isValidType = true;
		}

		if(isValidType){	//If valid proceed
			$(".infoContent-block").css("display", "block");  	//Set the css property of the info content div visisble.
			$(".infoType-block").css("display","none");	 //Set the css property of display to none. 
	
			heapType = $('.infoInput').val(); //Assigns the user's input for the heap tree's type.
		
			heap = new BinaryHeap(heapType);	//Instantiates the heap data structure object.
		}

		else{	//Otherwise be nice and give a helpful message.
			$('.infoType-block .popup').show();
			$('.infoType-block .popup').delay(3000).fadeOut();			
		}
	});

	$(".infoContent-block .add-button").on("click",function(){
		$(".infoContent-block input").attr("placeholder", "1..2..3..4..etc").val(""); //Set content block to none 
	});
	
	$(".infoContent-block .remove-button").on("click",function(){
		$(".infoContent-block input").attr("placeholder", "1..2..3..4..etc").val(""); //Set content block to none 
	});

	$(".restart-button").on("click",function(){ //When user clicks the restart button. 
		$(".infoContent-block input").attr("placeholder", "1..2..3..4..etc").val(""); //Set content block to none 
		$(".infoContent-block").css("display","none");
		
		$(".infoType-block input").attr("placeholder", "max or min").val(""); //Set input again to visisble 
		$(".infoType-block").css("display","block");
		
		$('canvas').attr({   //Sets the canvas element with the dimensions of the parent div. 
			'width': 1335,
			'height': 400
		});

		$('.myCanvas').outerHeight(400);
		$('.myCanvas').outerWidth(1335);
	});
	
	function adjustContent(){	//When the parent div grows increases the 
		var divHeight = $('.myCanvas').outerHeight();

		var divWidth = $('.myCanvas').outerWidth();
		
		var heightChange = Math.abs(divHeight - $('canvas').height()); 
		
		$('canvas').attr({
			'width': divWidth,
			'height': divHeight
		});
		
		$('.infoContent-block').css('top',heightChange+'px');
	}

	function drawTree(x1,y1,position,currentLvl){	//main function for drawing the Binary Heap Tree onto the canvas.
		var level_distances = [250,125,62.5,31.25,15.625,7.8125,3.90625,1.953125]; //Used to space the nodes.

		if(heap.get(position) != null){
			var l_x2 = x1-level_distances[currentLvl];	//Sets the x position of left child.
			var r_x2 = x1+level_distances[currentLvl];	//Sets the x position of right child.
			var y2 = y1+25; 	//Sets height of the next child.

			if(heap.get(2*position+1) != null){	//If the left child is there
				drawConnection(x1, y1,l_x2,y2);	//Connect from parent the left child.
				drawTree(l_x2,y2,2*position+1,currentLvl+1);	//Tranverses the left tree
			}

			if(heap.get(2*position+2) != null){	//If the right child is there
				drawConnection(x1, y1,r_x2,y2);	//Connect with parent the right child.
				drawTree(r_x2,y2,2*position+2,currentLvl+1);	//Tranverses the right tree.
			}
			
			var currentNode = heap.get(position);	//Get the current node and draw it.
			drawNode(currentNode, x1, y1);	//Draw node.
		}							
	}

	function drawConnection(x1, y1, x2, y2){ 	//Function used to draw connections between two nodes 
		ctx.strokeStyle = 'black';  //Sets the line connecting the two nodes black.
		ctx.lineWidth = 2;		//Sets the line width of the circle.
		ctx.beginPath();		//Starts the path. 
		ctx.moveTo(x1-15,y1);	//Starting from position(x1,y1)
		ctx.lineTo(x2+15,y2);	//to position(x2,y2)
		ctx.closePath();	//closes path.
		ctx.stroke();		//Draws the stroke of the path.
	}

	function drawNode(content, posX, posY){		//Function used to draw the node for the tree.
		ctx.beginPath();	//Starts the path for the drawing on canvas.
		ctx.lineWidth = 5;	//Sets the line width of the circle.
		ctx.arc(posX,posY,20,0,2*Math.PI);	//Draws the arc of 2PI.
		ctx.fillStyle = '#3399FF'; 	//Sets the filling color to light blue.
		ctx.fill(); 	//Fills in the circle.
		ctx.lineWidth = 5;	//Sets the line width of the circle.
		ctx.font = '15px Lato';	//Gives the font of the content.
		ctx.fillStyle = 'white';	//Gives the text a white color fill.
		ctx.textAlign = 'center';	//Centers the text.
		ctx.fillText(content,posX, posY+4);	//Fills the text in into the circle.
	}

	/*
	//Use this to compare and make sure everything is following the rules.
	drawConnection(c.width/2, 25,(c.width/2)-250,25+25);
	drawConnection(c.width/2, 25,(c.width/2)+250,25+25);
	drawConnection((c.width/2)-250,50,(c.width/2)-125-250,75);
	drawConnection((c.width/2)-250,50,(c.width/2)+125-250,75);
	drawConnection((c.width/2)+250,50,(c.width/2)-125+250,75);
	drawConnection((c.width/2)+250,50,(c.width/2)+125+250,75);
	

	drawNode('250', c.width/2, 25); //level 0 or root
	drawNode('100', (c.width/2)-250,50); //level 1.
	drawNode('10',(c.width/2)+250,50); // level 1 
	drawNode('2', (c.width/2)-125-250,75); // level 2 
	drawNode('13',(c.width/2)+125-250,75); // level 2  
	drawNode('50', (c.width/2)-125+250,75); // level 2 
	drawNode('80',(c.width/2)+125+250,75); // level 2  


	ctx.translate(1.5,1.5); 
	var centerX = c.width / 2; 
	var centerY = 25; 
	var radius = 25; 

	ctx.beginPath(); 
	ctx.arc(centerX,centerY,radius,0,2*Math.PI);
	ctx.fillStyle = '#3399FF'; 
	ctx.fill(); 
	ctx.lineWidth = 2; 
	ctx.strokeStyle = '#246BB2';
	ctx.stroke();
	ctx.font = '15px Lato';

	ctx.fillStyle = 'white';
	var content = "250";
	ctx.textAlign = 'center';
	ctx.fillText(content,centerX, centerY+4);
	ctx.closePath();

////////////////////////////////////////////////////////

	ctx.translate(1.5,1.5); 
	var centerX = (c.width / 2)-250; 
	var centerY = 75; 
	var radius = 25; 

	ctx.beginPath(); 
	ctx.arc(centerX,centerY,radius,0,2*Math.PI);
	ctx.fillStyle = '#3399FF'; 
	ctx.fill(); 
	ctx.lineWidth = 2; 
	ctx.strokeStyle = '#246BB2';
	ctx.stroke();
	ctx.font = '15px Lato';

	ctx.fillStyle = 'white';
	var content = "20";
	ctx.textAlign = 'center';
	ctx.fillText(content,centerX, centerY+4);
	ctx.closePath();

	ctx.translate(1.5,1.5); 
	var centerX = (c.width / 2)+250; 
	var centerY = 75; 
	var radius = 25; 

	ctx.beginPath(); 
	ctx.arc(centerX,centerY,radius,0,2*Math.PI);
	ctx.fillStyle = '#3399FF'; 
	ctx.fill(); 
	ctx.lineWidth = 2; 
	ctx.strokeStyle = '#246BB2';
	ctx.stroke();
	ctx.font = '15px Lato';

	ctx.fillStyle = 'white';
	var content = "20";
	ctx.textAlign = 'center';
	ctx.fillText(content,centerX, centerY+4);
	ctx.closePath();*/
});