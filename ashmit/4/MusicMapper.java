package p4_dsbdal;

import java.io.IOException;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Mapper;

public class MusicMapper
        extends Mapper<LongWritable, Text, Text, Text>
{

    public void map(LongWritable key,
                    Text value,
                    Context context)
            throws IOException, InterruptedException
    {

        String line = value.toString();

        // Skip header
        if (line.contains("UserId"))
        {
            return;
        }

        String[] data = line.split(",");

        // check columns
        if (data.length < 5)
        {
            return;
        }

        String trackId = data[1];
        String radio = data[3];
        String skip = data[4];

        // send trackId as key
        context.write(
                new Text(trackId),
                new Text(radio + "," + skip)
        );
    }
}