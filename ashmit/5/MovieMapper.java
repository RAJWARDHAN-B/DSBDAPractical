package p5_dsbdal;

import java.io.IOException;

import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import org.apache.hadoop.mapreduce.Mapper;

public class MovieMapper
        extends Mapper<LongWritable,
                       Text,
                       Text,
                       FloatWritable>
{

    public void map(LongWritable key,
                    Text value,
                    Context context)
            throws IOException, InterruptedException
    {

        String line = value.toString();

        // Skip header
        if (line.contains("userId"))
        {
            return;
        }

        String[] data = line.split(",");

        // check columns
        if (data.length < 3)
        {
            return;
        }

        try
        {

            String movieId = data[1];

            float rating =
                    Float.parseFloat(data[2]);

            // send movieId and rating
            context.write(
                    new Text(movieId),
                    new FloatWritable(rating)
            );

        }
        catch (Exception e)
        {

            // skip invalid rows
        }
    }
}