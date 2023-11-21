package main

import (
	"bufio"
	"fmt"
	"os"
	"os/exec"
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
		//fmt.Println(userInput)
		fmt.Println("=>")

		if strings.Compare("exit", userInput) == 0 {
			os.Exit(0)
		}

		var commandString []string = strings.Split(userInput, " ")

		if strings.Compare(commandString[0], "checkConnect") == 0 {
			commandOutput := execPINGCommand(commandString[1])
			fmt.Println(commandOutput)
		} else {
			fmt.Println("command not supported by CLI")
		}
		fmt.Println("=>")
	}
}

func execPINGCommand(cmdParam string) string {
	// Execute OS command ping
	if c, err := exec.Command("cmd", "c", "ping", "-n", "3", cmdParam).CombinedOutput(); err != nil {
		s := "Error! Command execution faild"
		return (s)
	} else {
		return string(c)
	}
}
