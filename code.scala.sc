//> using scala 3.6
//> using dep "org.scalanlp::breeze:2.1.0"

val n = args.headOption.map(_.toInt).getOrElse(1000)

import breeze.linalg._
import breeze.numerics._

// compute elapsed time
inline def time[R](block: => R): R = {
  val t0 = System.nanoTime()
  val result = block
  val t1 = System.nanoTime()
  val millis = (t1 - t0) / 1000000
  println("Elapsed time: " + millis + "ms")
  result
}

time {
  println("preparing matrix")
  val mm = CSCMatrix.rand(n, n).map(d => if d > 0.05 then 0.0 else 1.0)

  println("computing eigenvectors")
  val ev = eig(mm.t)
  println("computing abs")
  val evabs = ev.eigenvectors(::, 0).map(_.abs)

  println(evabs)
}
