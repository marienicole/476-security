package main

import (
	"fmt"

	"github.com/google/gopacket"
	"github.com/google/gopacket/layers"
	"github.com/google/gopacket/pcap"
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
	ipLayer := p.Layer(layers.LayerTypeIPv4)
	tcpLayer := p.Layer(layers.LayerTypeTCP)
	ip, _ := ipLayer.(*layers.IPv4)
	tcp, _ := tcpLayer.(*layers.TCP)
	synAcks := make(map[string]int)
	syns := make(map[string]int)

	if tcpLayer != nil {
		// fmt.Printf("\nSrc IP: %s, Dest IP: %s", ip.SrcIP, ip.DstIP)
		// fmt.Printf("\nSyn? %t", tcp.SYN)
		if tcp.SYN == true {
			if synAcks[ip.SrcIP.String()] != 0 {
				synAcks[ip.SrcIP.String()]++
				syns[ip.SrcIP.String()]++
			} else {
				synAcks[ip.SrcIP.String()] = 1
				syns[ip.SrcIP.String()] = 1
			}
		} else if tcp.ACK == true {
			if synAcks[ip.SrcIP.String()] != 0 {
				synAcks[ip.SrcIP.String()]++
			} else {
				synAcks[ip.SrcIP.String()] = 1
			}
		}
	}

	for ip, number := range syns {
		if number >= 3*synAcks[ip] {
			fmt.Print("wooooo")
		}

	}

	// the last 8 characters of array 1 are the source and dest IPs
	// &{{[69 0 5 220 117 31 32 0 62 17 132 135 128 3 70 97 128 3 23 3] [8 1 3 32 32 136 113 18]} 4 5 0 1500 29983 MF 0 62 UDP 33927 128.3.70.97 128.3.23.3 [] []}
	// Sender: 128.3.70.97
	// REceiver: 128.3.23.1
}
