package main

import (
	"bufio"
	"fmt"
	"os"
	//"os/exec"
	//"strings"
)

func main() {
	fmt.Println("Cloud CLI")
	fmt.Println("---------------------")
	fmt.Println("=>")

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		userInput := scanner.Text()
		fmt.Println(userInput)
		fmt.Println("=>")
	}
}

func execPINGCommand(cmdParam string) string {
	return "execPINGCommand"
}
