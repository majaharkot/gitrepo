function setup() {
  // put setup code here
  createCanvas(1000, 480);
}

function draw() {
  // put drawing code here
/* strokeWeight (4);
   stroke ('#FF00BF');
   fill (254, 42, 248);
   ellipse(50, 50, 80, 80);

   strokeWeight (2);
   stroke ('#7745FF');
   fill (186, 73, 255);
   ellipse(100, 100, 200, 80);

   strokeWeight (6);
   stroke ('#FFAEFA');
   fill (255, 204, 221);
   rect(30, 20, 55, 55); */

  noFill();
  noStroke();
   if (mouseIsPressed) {
     if (mouseButton === LEFT) {
      r = random(255);
      g = random(255);
      b = random(255);
      strokeWeight(20);
      fill(r, g, b, 127);
      stroke(r, g, b);
     }
     if (mouseButton === CENTER) {
      strokeWeight(20);
      fill(255, 255, 255);
      stroke(255, 255, 255);
      rect(mouseX-10, mouseY-10, 20, 20);
     }
   } else {
     noFill ();
     noStroke();
   }
   point (mouseX, mouseY);
}
