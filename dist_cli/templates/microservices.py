def get_logic_template(name: str):
      template = f"""from setup import Setup
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def {name}(message: bytes, config: Setup):
      try:
            ... # Add your code here
      except Exception as err:
            logger.error(err)
            # Handle error
      """
      return template


def get_main_template(name: str):
      template = f"""import asyncio
from setup import Setup
from service.logic import {name}

config = Setup()

async def main():
      try:
            await config.setup_amqp_connection()
            await config.setup_broadcaster_connection()
            
            await config._amqp_consumer._consume(
                  '{name}', # Queue name
                  {name},
                  config
            )
      finally:
            await config.close_amqp_connection()
            await config.close_broadcaster_connection()
            await config.close_redis_connection()

if __name__ == '__main__':
      loop = asyncio.new_event_loop()
      asyncio.set_event_loop(loop)
      loop.run_until_complete(main())
      """
      return template