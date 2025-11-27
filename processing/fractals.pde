ArrayList<Particle> particles;
float angleX = 0;
float angleY = 0;
float lastMouseX, lastMouseY;

void setup() {
  // 3D rendering
  size(750, 750, P3D);
  // HSB for easier color manipulation
  colorMode(HSB, 360, 100, 100);
  particles = new ArrayList<Particle>();
  for (int i = 0; i < 500; i++) {
    particles.add(new Particle());
  }
}

void draw() {
  background(0); // black
  lights();
  if (mousePressed) {
    float dx = mouseX - lastMouseX;
    float dy = mouseY - lastMouseY;
    angleY += radians(dx); // rotate around the Y-axis
    angleX += radians(dy); // rotate around the X-axis
  }
  lastMouseX = mouseX;
  lastMouseY = mouseY;
  
  // center and apply rotations
  translate(width / 2, height / 2, 0);
  rotateX(angleX);
  rotateY(angleY);
  
  for (Particle p : particles) {
    p.update();
    p.display();
  }
}

class Particle {
  PVector pos;
  PVector vel;
  PVector acc;
  float maxSpeed = 3;
  float maxForce = 0.05;
  
  Particle() {
    pos = new PVector(random(-width/2, width/2), random(-height/2, height/2), random(-width/2, width/2));
    vel = new PVector();
    acc = new PVector();
  }

  void update() {
    // create the two invisible attractors
    PVector attractor1 = new PVector(sin(frameCount * 0.01) * 200, cos(frameCount * 0.01) * 200, sin(frameCount * 0.005) * 200);
    PVector attractor2 = new PVector(cos(frameCount * 0.01) * 200, sin(frameCount * 0.01) * 200, cos(frameCount * 0.005) * 200);
    
    // forces pulling the particle towards the attractors
    PVector force1 = PVector.sub(attractor1, pos);
    PVector force2 = PVector.sub(attractor2, pos);
    
    // normalize and scale the forces
    force1.normalize().mult(maxForce);
    force2.normalize().mult(maxForce);
    
    // apply forces to particle's acceleration
    acc.add(force1).add(force2);
    
    vel.add(acc);
    vel.limit(maxSpeed);
    pos.add(vel);
    
    // reset acceleration for next frame
    acc.mult(0);
  }
  
  void display() {
    float hue = (pos.x + pos.y + frameCount * 0.5) % 360;
    stroke(hue, 150, 150, 150);
    strokeWeight(4);
   
    point(pos.x, pos.y, pos.z);
    
    // create symmetry by drawing mirrored particles across all axes
    point(-pos.x, pos.y, pos.z);
    point(pos.x, -pos.y, pos.z);
    point(pos.x, pos.y, -pos.z);
    point(-pos.x, -pos.y, pos.z);
    point(-pos.x, pos.y, -pos.z);
    point(pos.x, -pos.y, -pos.z);
    point(-pos.x, -pos.y, -pos.z);
  }
}