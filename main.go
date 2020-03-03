package main

import (
        "fmt"
        "time"

        "gobot.io/x/gobot"
        "gobot.io/x/gobot/platforms/dji/tello"
)

func main() {
	fmt.Println("Inicio")
        drone := tello.NewDriver("8888")

        work := func() {
        drone.TakeOff()

			 gobot.After(5*time.Second, func() {
         fmt.Println("deberia subir")
         drone.Up(50)
         gobot.After(5*time.Second, func() {
           fmt.Println("deberia aterrizar")
           drone.Land()
         })
       })

        }

        robot := gobot.NewRobot("tello",
                []gobot.Connection{},
                []gobot.Device{drone},
                work,
        )

        robot.Start()
}
