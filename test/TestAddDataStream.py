import io
import unittest

host  = ''  # host url
token = ''  # auth token


class TestAddDataStream(unittest.TestCase):

    def setUp(self):
        pass

    def test_add_json_data_stream_for_single_thing(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'iso_8601'
        }
        eventbuffer.set_name('Motor Health')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer, options)
            pipeline = Schemas.Pipeline()
            signals  = {
                'current': 'Numeric',
                'vibration': 'Numeric',
                'state': 'Categorical'
            }
            assessment = Schemas.Assessment()
            assessment.set_name('Health') \
                .set_input_signals(['current', 'vibration', 'state'])
            pipeline.set_name('Motor Health 1') \
                .set_eventbuffer(eventbuffer.get_id()) \
                .set_input_signals(signals) \
                .set_thing_name('Motor') \
                .set_assessment(assessment)

            try:
                created_pipeline = fclient.create_pipeline(pipeline)
                try:
                    data = io.open('./data.json')
                    response = fclient.add_input_stream(created_pipeline.get_id(), 'json', {}, data)

                    self.assertNotEqual(response['__$id'], None, 'Cannot add input data to eventbuffer')

                    # tear down
                    try:
                        fclient.delete_pipeline(created_pipeline.get_id())
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                except Exception as e:
                    print(e.message)
                    self.assertEqual(0, 1, 'Cannot add input data to eventbuffer')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create pipeline')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

    def test_add_csv_data_stream_for_single_thing(self):
        fclient = FClient(host=host, token=token)
        eventbuffer = Schemas.Eventbuffer()
        options = {
            'timeIdentifier' : 'time',
            'timeFormat'     : 'iso_8601'
        }
        eventbuffer.set_name('Motor Health')
        try:
            eventbuffer = fclient.create_eventbuffer(eventbuffer, options)
            pipeline = Schemas.Pipeline()
            signals  = {
                'current': 'Numeric',
                'vibration': 'Numeric',
                'state': 'Categorical'
            }
            assessment = Schemas.Assessment()
            assessment.set_name('Health') \
                .set_input_signals(['current', 'vibration', 'state'])
            pipeline.set_name('Motor Health 1') \
                .set_eventbuffer(eventbuffer.get_id()) \
                .set_input_signals(signals) \
                .set_thing_name('Motor') \
                .set_assessment(assessment)

            try:
                created_pipeline = fclient.create_pipeline(pipeline)
                try:
                    data = io.open('./data.csv')
                    response = fclient.add_input_stream(created_pipeline.get_id(), 'csv', {}, data)

                    self.assertNotEqual(response['__$id'], None, 'Cannot add input data to eventbuffer')

                    # tear down
                    try:
                        fclient.delete_pipeline(created_pipeline.get_id())
                        fclient.delete_eventbuffer(eventbuffer.get_id())
                    except Exception as e:
                        pass
                except Exception as e:
                    print(e.message)
                    self.assertEqual(0, 1, 'Cannot add input data to eventbuffer')
            except Exception as e:
                print(e.message)
                self.assertEqual(0, 1, 'Cannot create pipeline')
        except Exception as e:
            print(e.message)
            self.assertEqual(0, 1, 'Cannot create eventbuffer')

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(
            path.dirname(
                path.dirname(
                    path.abspath(__file__)
                )
            )
        )
        from falkonryclient import schemas as Schemas
        from falkonryclient import client as FClient
    else:
        from ..falkonryclient import schemas as Schemas
        from ..falkonryclient import client as FClient
    unittest.main()
