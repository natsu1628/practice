package com.personal.practice;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
public class BookController {
    private List<Book> bookList = new ArrayList<>();

    @GetMapping("/books/all")
    public List<Book> getAllBooks() {
        return bookList;
    }

    @GetMapping("/books/{isbn}")
    public Book getBook(@PathVariable String isbn) {
        if (isbn == null) {
            throw new IllegalArgumentException("Book ISBN cannot be null");
        }
        Book bookReturn = null;
        for(Book book: bookList) {
            if (book.getIsbn().equals(isbn)) {
                bookReturn = book;
            }
        }
        return bookReturn;
    }

    @PostMapping("/books")
    public Book addBook(@RequestBody Book book) {
        if (book.getIsbn() == null) {
            throw new IllegalArgumentException("Book ISBN cannot be null");
        }
        bookList.add(book);
        return book;
    }
}
