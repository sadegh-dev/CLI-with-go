package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	//"os/exec"
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

		if strings.Compare("exit", userInput) == 0 {
			os.Exit(0)
		}
	}

}

func execPINGCommand(cmdParam string) string {
	return "execPINGCommand"
}
