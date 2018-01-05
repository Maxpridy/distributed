import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('210.100.235.128', 3456, loop=loop)

    print('Send: %r' % message)
    for word in message:
        writer.write(word.encode())


    data = await reader.read(1000)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()

data = "qwer asdf zxcv"
message = data.split(" ")
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()
