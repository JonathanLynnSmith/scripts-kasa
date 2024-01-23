import asyncio
import sys
from kasa import SmartPlug

async def control_kasa_device(host_ip, state):
    try:
        # Connect to the Kasa device
        device = SmartPlug(host_ip)

        # Set the state based on the input parameter
        if state.lower() == 'on':
            await device.turn_on()
        elif state.lower() == 'off':
            await device.turn_off()
        else:
            raise ValueError("Invalid state. Use 'on' or 'off'.")
        print(f"Action completed successfully. Device is now {state}.")
        return 0
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        return error_message

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python kasa_logic.py <host_ip> <state>")
        sys.exit(1)

    host_ip, state = sys.argv[1:]
    
    # Create an event loop
    loop = asyncio.get_event_loop()
    
    # Run the asynchronous task until completion
    result = loop.run_until_complete(control_kasa_device(host_ip, state))
    
    # Close the event loop
    loop.close()
    
    sys.exit(result)
