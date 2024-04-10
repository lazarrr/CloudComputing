using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

[ApiController]
[Route("[controller]")]
public class TodoController : ControllerBase
{
    private readonly ApiDbContext _context;
    public TodoController(ApiDbContext context)
    {
        _context = context;
    }

    [HttpGet(Name = "GetAllTodos")]
    public async Task<IActionResult> Get()
    {
        var todos = await _context.Todos.ToListAsync();
       return Ok(todos);
    }

    [HttpPost(Name = "AddToTodos")]
    public async Task<IActionResult> Post([FromBody] Todo todo)
    {
        await _context.Todos.AddAsync(todo);
        await _context.SaveChangesAsync();
        return Ok();
    }

    [HttpPut(Name = "UpdateTodos")]
    public async Task<IActionResult> put([FromBody] Todo todo)
    {
         var _todo = await _context.Todos.Where(x => x.Id == todo.Id).FirstOrDefaultAsync();
        
        if(_todo == null)
            return BadRequest("Todo not found");

        _todo.name = todo.name;
        _todo.count = todo.count;

        _context.Todos.Update(_todo);
        await _context.SaveChangesAsync();
        return Ok();
    }

    [HttpDelete(Name = "DeleteTodos")]
    public async Task<IActionResult> Delete([FromBody] long id)
    {
        var todo = await _context.Todos.Where(x => x.Id == id).FirstOrDefaultAsync();
        
        if(todo == null)
            return BadRequest("Todo not found");

        _context.Todos.Remove(todo);
        await _context.SaveChangesAsync();

        return Ok();
    }

}