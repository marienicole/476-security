package main

import (
	// 	"fmt"
	// 	"os"
	"fmt"

	"github.com/google/gopacket"
	"github.com/google/gopacket/pcap"
	// 	"io"
	// "io/ioutil"
)

func main() {
	// fmt.Print("yeet")
	if handle, err := pcap.OpenOffline("security_assn4.pcap"); err != nil {
		panic(err)
	} else {
		packetSource := gopacket.NewPacketSource(handle, handle.LinkType())
		for packet := range packetSource.Packets() {
			handlePacket(packet) // Do something with a packet here.
		}
	}
}

func handlePacket(p gopacket.Packet) {
	fmt.Print(p)
}
